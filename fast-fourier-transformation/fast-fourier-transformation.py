# %%
import numpy as np
import matplotlib.pyplot as plt

from scipy.io.wavfile import write
from scipy.io.wavfile import read

from scipy.io import wavfile
import scipy.io

sampleRate, odevWav = scipy.io.wavfile.read("Ornek.wav")
length = odevWav.shape[0] / sampleRate
print(f"length = {length}s")


plt.plot(odevWav)
plt.title("ornek dosyası grafiği")
plt.show()

parcalar = np.array_split(odevWav, 11)



telNo = list()

for i in range(11):
    yf = np.fft.fft(parcalar[i])
    xf = np.fft.fftfreq(len(parcalar[i]), 1 / sampleRate)

    posFreq = xf[xf >= 0]
    yf = yf[xf >= 0]
    magnitudes = np.abs(yf)

    n = 3
    idx = np.argsort(magnitudes)[::-1][:n]
    peakFreq = xf[idx]
    print(f"basilan {i+1}. tusun frekanslari:")
    print(peakFreq)
    peakFreq = np.sort(peakFreq)

    if i == 7:
        tmp = peakFreq[1]
        peakFreq[1] = peakFreq[2]
        peakFreq[2] = tmp

    plt.plot(posFreq, np.abs(yf))
    plt.title(f"{i+1}. tusun frekanslari")
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

    if abs(peakFreq[1]-1209) < 5:
        if abs(peakFreq[2]-697) < 5:
            telNo.append(1)
            print("1")
        elif abs(peakFreq[2]-770) < 5:
            telNo.append(4)
            print("4")
        elif abs(peakFreq[2]-852) < 5:
            telNo.append(7)
            print("7")
        elif abs(peakFreq[2]-941) < 5:
            telNo.append('*')
            print("*")
    elif abs(peakFreq[1]-1336) < 5:
        if abs(peakFreq[2]-697) < 5:
            telNo.append(2)
            print("2")
        elif abs(peakFreq[2]-770) < 15:
            telNo.append(5)
            print("5")
        elif abs(peakFreq[2]-852) < 5:
            telNo.append(8)
            print("8")
        elif abs(peakFreq[2]-941) < 5:
            telNo.append(0)
            print("0")
    elif abs(peakFreq[1]-1477) < 5:
        if abs(peakFreq[2]-697) < 5:
            telNo.append(3)
            print("3")
        elif abs(peakFreq[2]-770) < 5:
            telNo.append(6)
            print("6")
        elif abs(peakFreq[2]-852) < 5:
            telNo.append(9)
            print("9")
        elif abs(peakFreq[2]-941) < 5:
            telNo.append('#')
            print("#")

print("***********")
for k in range(len(telNo)):
    print(telNo[k])
#print(f"telefon numarasi:{telNo}")

#telefon numarasının kodlanması
# 0 559 398 09 86
amp = 10
fs = 8000
t = 0.1
sample = np.linspace(0, t, int(fs*t))


# 0
f1_a = 1336
f1_b = 941
sin0 = amp*(np.sin(2*np.pi*f1_a*sample)+np.sin(2*np.pi*f1_b*sample))
# 5
f2_a = 1336
f2_b = 770
sin5 = amp*(np.sin(2*np.pi*f2_a*sample)+np.sin(2*np.pi*f2_b*sample))
# 3
f3_a = 1477
f3_b = 697
sin3 = amp*(np.sin(2*np.pi*f3_a*sample)+np.sin(2*np.pi*f3_b*sample))
# 9
f4_a = 1477
f4_b = 852
sin9 = amp*(np.sin(2*np.pi*f4_a*sample)+np.sin(2*np.pi*f4_b*sample))
# 6
f5_a = 1477
f5_b = 770
sin6 = amp*(np.sin(2*np.pi*f5_a*sample)+np.sin(2*np.pi*f5_b*sample))
# 8
f6_a = 1336
f6_b = 852
sin8 = amp*(np.sin(2*np.pi*f6_a*sample)+np.sin(2*np.pi*f6_b*sample))
# silence
sinS = 0*np.sin(2*np.pi*f6_a*sample)+0*np.sin(2*np.pi*f6_b*sample)

myNum = np.concatenate((sin0, sinS, sin5, sinS, sin5, sinS, sin9, sinS, sin3,
                       sinS, sin9, sinS, sin8, sinS, sin0, sinS, sin9, sinS, sin8, sinS, sin6, sinS))

myNum = myNum / np.max(np.abs(myNum))
myNum = myNum * 32767
myNum = myNum.astype(np.int16)

write("05593980986.wav", fs, myNum)

plt.plot(myNum)
plt.title("myNum ses dosyası")
plt.xlabel("sample")
plt.ylabel("amplitude")
plt.show()

numSampleRate, myNum = scipy.io.wavfile.read("05593980986.wav")
parcalar = np.array_split(myNum, 11)


telNo = list()

for i in range(11):
    yf = np.fft.fft(parcalar[i])
    xf = np.fft.fftfreq(len(parcalar[i]), 1 / sampleRate)

    posFreq = xf[xf >= 0]
    yf = yf[xf >= 0]
    magnitudes = np.abs(yf)
    n=3
    idx = np.argsort(magnitudes)[::-1][:n]
    peakFreq = xf[idx]
    peakFreq = np.sort(peakFreq)


    print(f"basilan {i+1}. tusun frekanslari:")
    print(peakFreq)

    plt.plot(posFreq, np.abs(yf))
    plt.title(f"{i+1}. tusun frekanslari(benim telefon numaram)")
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

    

    freqList=list()
    m=0
    for g in range(3):
        if abs(peakFreq[g]-1209) < 10:
            if 1209 not in freqList:
               freqList.append(1209)
                
        elif abs(peakFreq[g]-697) < 10:
             if 697 not in freqList:
                 freqList.append(697)
                
        elif abs(peakFreq[g]-770) < 10:
            if 770 not in freqList:
                 freqList.append(770)
                
        elif abs(peakFreq[g]-852) < 10:
            if 852 not in freqList:
                 freqList.append(852)
                
        elif abs(peakFreq[g]-941) < 10:
            if 941 not in freqList:
                 freqList.append(941)
                
        elif abs(peakFreq[g]-1336) < 10:
            if 1336 not in freqList:
                 freqList.append(1336)
                
        elif abs(peakFreq[g]-1477) < 10:
            if 1477 not in freqList:
                 freqList.append(1477)
                

    if freqList[0]<freqList[1]:
        tmp=freqList[0]
        freqList[0]=freqList[1]
        freqList[1]=tmp



    if abs(freqList[0]-1209) < 5:
        if abs(freqList[1]-697) < 5:
            telNo.append(1)
            print("1")
        elif abs(freqList[1]-770) < 5:
            telNo.append(4)
            print("4")
        elif abs(freqList[1]-852) < 5:
            telNo.append(7)
            print("7")
        elif abs(freqList[1]-941) < 5:
            telNo.append('*')
            print("*")
    elif abs(freqList[0]-1336) < 5:
        if abs(freqList[1]-697) < 5:
            telNo.append(2)
            print("2")
        elif abs(freqList[1]-770) < 15:
            telNo.append(5)
            print("5")
        elif abs(freqList[1]-852) < 5:
            telNo.append(8)
            print("8")
        elif abs(freqList[1]-941) < 5:
            telNo.append(0)
            print("0")
    elif abs(freqList[0]-1477) < 5:
        if abs(freqList[1]-697) < 5:
            telNo.append(3)
            print("3")
        elif abs(freqList[1]-770) < 5:
            telNo.append(6)
            print("6")
        elif abs(freqList[1]-852) < 5:
            telNo.append(9)
            print("9")
        elif abs(freqList[1]-941) < 5:
            telNo.append('#')
            print("#")

print("***********")
print(f"telefon numarasi:{telNo}")





# %%
