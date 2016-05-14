# ohchr_case_analysis
Analyzing OHCHR cases.

Brief Explanation:
1) The code in the downloadcases directory uses scrapy (http://scrapy.org/) to download the OHCHR cases.
2) The code in the code directory so far does two things:
    a) pdf_to_xml is a simple loop to conver the pdfs to xml files. The xml files contain blocks of text with position and other information. This is a very raw form which needs to be processed to be used. For example, one has to "infer" where paragraphs begin and end.
    b) xml_to_txt to which takes that raw xml and converts it to two sets of text files per case - one for the body and one for the footnotes.

Next Steps:
1) Deal with footers. Footners come and and mess up the analysis. Right now, they are just treated as text.
2) Add comments. The code is not commented at all.
3) Change the txt format to a nicer xml format with a document, paragraphs, and footnotes.
4) Stip out data about countries, etc... to analyze.
