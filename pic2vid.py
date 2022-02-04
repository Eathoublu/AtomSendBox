import os
def main():
    path = 'epc'
    target = 'video.mp4'
    # os.chdir(path)
    # os.system("ffmpeg  -r 25 -pattern_type glob -i '{}/*.png' -c:v libx264 out.mp4".format(path))
    # os.system(" ffmpeg -f image2 -i {}/%d.png -vcodec libx264 -r 10 tt.mp4".format(path))
    os.system("cat {}/* | ffmpeg -framerate 0.3 -f image2pipe -i - -c:v copy {}".format(path, target))

if __name__ == '__main__':
    main()