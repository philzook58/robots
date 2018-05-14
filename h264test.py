import h264decode

decoder = h264decode.Decoder(avccPacket)
for frame in frameGenerator:
    yuv = decoder.decodeFrame(frame)
    print "Read frame of %dx%d pixels" % (yuv.width, yuv.height)
    # e.g. rendering with pygame:
    overlay.display((yuv.y, yuv.u, yuv.v))