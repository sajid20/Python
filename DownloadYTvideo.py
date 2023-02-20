from pytube import YouTube

# Create a YouTube object for the video you want to download
yt = YouTube("https://www.youtube.com/watch?v=wGRRHmpZYOQ")

# Select the highest quality stream
stream = yt.streams.get_highest_resolution()

# Download the video to your current working directory
stream.download()
