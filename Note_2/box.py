#!/usr/bin/python

sentence = raw_input("Sentence: ");

screen_width = 80;
text_width   = len(sentence);
box_width    = text_width + 2;
left_margin  = (screen_width - box_width) / 2;

print;
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+';
print ' ' * left_margin + '|' + ' ' * text_width      + '|';
print ' ' * left_margin + '|' +       sentence        + '|';
print ' ' * left_margin + '|' + ' ' * text_width      + '|';
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+';
print;

# result
'''
Sentence: I am a box, and I will print a sentence with a box

              +--------------------------------------------------+
              |                                                  |
              |I am a box, and I will print a sentence with a box|
              |                                                  |
              +--------------------------------------------------+

'''
