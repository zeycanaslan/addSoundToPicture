from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

# Resim ve ses dosyalarının yollarını belirtin
resim_yolu = "picture.jpeg"
ses_yolu = "stan-long-version-ft-dido (1).mp3"
cikti_yolu = "output.mp4"

# Resim klibini oluşturun
resim_clip = ImageClip(resim_yolu, duration=24)  # Resmin görüntüleneceği süreyi belirtin
resim_clip.fps = 24  # FPS değerini belirtin

# Ses klibini yükleyin
ses_clip = AudioFileClip(ses_yolu)

# Resim klibine sesi ekleyin
resim_clip = resim_clip.set_audio(ses_clip)

# Çıktıyı kaydedin
resim_clip.write_videofile(cikti_yolu, codec="libx264", audio_codec="aac")
