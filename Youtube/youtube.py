import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            videosData = json.load(file)
            return videosData
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
   
def list_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos):
        print(f"{index + 1}: {video['name'], video['time']}")
    print("*" * 70)
    print("\n")


def add_videos(videos):
    name = input("Enter a video name: ")
    time = input("Enter a video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    # print("Add a video:")

def update_videos(videos):
    list_videos(videos)
    name = input("Enter a video name: ")
    newTime = input("Enter a new video time: ")
    number = int(input("Enter a video number: "))
    if number <= len(videos):
        videos[number - 1] = {'name': name, 'time': newTime}
        save_data_helper(videos)
    else:
        print("\n")
        print("*" *  70)
        print("Invalid number")
        print("*" * 70)
        print("\n")

    

def delete_videos(videos):
    list_videos(videos)
    number = int(input("Enter a video number: "))
    if number <= len(videos):
        del videos[number - 1]
        save_data_helper(videos)
    else:
        print("\n")
        print("*" *  70)
        print("Invalid number")
        print("*" * 70)
        print("\n")


def main():
    videos = load_data()
    # print("videos", videos)
    while True:
        print("Select a Number:")
        print("List all videos press 1:")
        print("Add a video press 2:")
        print("Update a video press 3:")
        print("Delete a video press 4:")
        print("Exit press 5:")
        choice = input("Enter a number: ")

        match choice:
            case '1':
                list_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()