# -*- coding: utf-8 -*-
"""
Created on Thu May 12 21:04:40 2016

@author: hari
"""

class Fragment:
    """
    page_number
    top, bottom, left, right
    text
    format - for later use
    """
    def __init__(self, page_number, xml_tag):
        self.page_number = page_number        
        self.top = int(xml_tag.xpath('./@top')[0])
        self.bottom = self.top + int(xml_tag.xpath('./@height')[0])
        self.left = int(xml_tag.xpath('./@left')[0])
        self.right = self.left + int(xml_tag.xpath('./@width')[0])
        self.text = unicode(self.actualText(xml_tag))
    
    def actualText(self, xml_tag):
        text_pieces = [x.strip() for x in xml_tag.xpath('.//text()')]
        actual_text = ' '.join(text_pieces)
        return(actual_text)
    
    @property
    def height(self):
        return(self.bottom - self.top)
    
    @property
    def width(self):
        return(self.right - self.left)

class Line:
    """
    page_number
    top, bottom, left, right
    text
    format - for later use
    fragments
    """
    def __init__(self, text_fragment):
        self.page_number = text_fragment.page_number
        self.top, self.bottom = text_fragment.top, text_fragment.bottom
        self.left, self.right = text_fragment.left, text_fragment.right
        self.texts_ = [(text_fragment.left, text_fragment.text)]
        self.text_fragments = [text_fragment]
    
    def canAddFragment(self, text_fragment):
        covered_height = max(self.bottom, text_fragment.bottom) - min(self.top, text_fragment.top)
        used_height = (text_fragment.bottom - text_fragment.top) + (self.bottom - self.top)
        overlap_height = used_height - covered_height
        percent_overlap = float(overlap_height)/min(text_fragment.bottom - text_fragment.top, self.bottom - self.top)
        if (percent_overlap > 0.5):
            return(True)
    
    def addFragment(self, text_fragment):
        self.top = min(self.top, text_fragment.top)
        self.bottom = max(self.bottom, text_fragment.bottom)
        self.left = min(self.left, text_fragment.left)
        self.right = max(self.right, text_fragment.right)
        self.texts_.append((text_fragment.left, text_fragment.text))
        self.text_fragments.append(text_fragment)
    
    @property
    def text(self):
        sorted_texts = [s[1] for s in sorted(self.texts_, key = lambda x: x[0])]
        return(' '.join(sorted_texts))
    
    @property
    def height(self):
        return(self.bottom - self.top)
    
    @property
    def width(self):
        return(self.right - self.left)

class Paragraph:
    """
    page_numbers
    top, bottom, left, right
    texts_
    format - for later use
    lines
    """
    
    def __init__(self, line):
        self.top, self.bottom = line.top, line.bottom
        self.left, self.right = line.left, line.bottom
        self.texts_ = [(line.top, line.text)]
        self.lines = [line]

    def addLine(self, line):
        self.top = min(self.top, line.top)
        self.bottom = max(self.bottom, line.bottom)
        self.left = min(self.left, line.left)
        self.right = max(self.right, line.right)
        self.texts_.append((line.top, line.text))
        self.lines.append(line)
    
    def merge(self, next_paragraph):
        for line in next_paragraph.lines:
            self.addLine(line)
    
    @property
    def text(self):
        sorted_texts = [s[1] for s in sorted(self.texts_, key = lambda x: x[0])]
        return(' '.join(sorted_texts))
    
    @property
    def height(self):
        return(self.bottom - self.top)
    
    @property
    def width(self):
        return(self.right - self.left)
