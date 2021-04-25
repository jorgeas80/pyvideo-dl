import tldextract
from pytube import YouTube
from twitter_dl import TwitterDownloader
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The url of the video to download')
    args = parser.parse_args()

    return args


def download_youtube(youtube_url):
    yt = YouTube(youtube_url)
    yt.streams.get_highest_resolution().download()


def download_twitter(tweet_url):
    td = TwitterDownloader(tweet_url)
    td.download()


if __name__ == '__main__':
    args = parse_arguments()

    ext = tldextract.extract(args.url)
    print(f"Will try to download video from {ext.domain}")
    if ext.domain == 'youtube':
        download_youtube(args.url)
    elif ext.domain == 'twitter':
        download_twitter(args.url)
    else:
        pass
    print("Finished")
