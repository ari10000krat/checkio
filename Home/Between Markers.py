def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    start_index = 0 if text.rfind(begin) == -1 else text.find(begin) + len(begin)  # End of the first sepatrator
    end_index = len(text) if text.find(end) == -1 else text.find(end)  # Begin of the second separator

    return text[start_index:end_index]

# def bigger_price(limit, data):
#     return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]
#
# def between_markers(text: str, begin: str, end: str) -> str:
#     if text.find(begin) > text.find(end) > -1:
#         return ''
#     return text.split(begin)[-1].split(end)[0]

if __name__ == '__main__':
    print('TEST #1 : ',between_markers("<head><title>My new site</title></head>",
                          "<title>", "</title>"))
    print('TEST #2 : ',between_markers('What is >apple<', '>', '<'))
    print('TEST #3 : ',between_markers('No[/b] hi', '[b]', '[/b]'))
    print('TEST #4 : ',between_markers('What is >ap ple<', '>', '<'))
    print('TEST #5 : ',between_markers('No [b]hi', '[b]', '[/b]'))
    print('TEST #6 : ',between_markers('No hi', '[b]', '[/b]'))
    print('TEST #7 : ',between_markers('No <hi>', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"

    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
