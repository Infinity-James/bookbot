def get_num_words(contents):
    try:
        words = contents.split()
        return len(words)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred: ", e)