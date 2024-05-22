from khmersegment import Segmenter

segmenter = Segmenter("-m km-5tag-seg-model")

print(segmenter("Hello មិនដឹងប្រាប់អ្នកណាទេ?", deep=False))
# => ['Hello', ' ', 'មិន', 'ដឹង', 'ប្រាប់', 'អ្នកណា', 'ទេ', '?']

print(segmenter("Hello មិនដឹងប្រាប់អ្នកណាទេ?", deep=True))
# => ['Hello', ' ', 'មិន', 'ដឹង', 'ប្រាប់', 'អ្នក', 'ណា', 'ទេ', '?']
