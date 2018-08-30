import alsaaudio as aa
import wave

FS = 44100 

fi     = wave.open("radar_movementnotraw.wav", "w")
fi.setnchannels(2)
fi.setsampwidth(2)
fi.setframerate(FS)

stream = aa.PCM(aa.PCM_CAPTURE, aa.PCM_NORMAL,cardindex = 1)
stream.setchannels(2)


stream.setrate(FS)
stream.setperiodsize(2000)

stream.setformat(aa.PCM_FORMAT_S16_LE)
t =0 
while t< 100:
	t+=1
	data = stream.read()
	print(data)
	fi.writeframes(data[1])
fi.close()
