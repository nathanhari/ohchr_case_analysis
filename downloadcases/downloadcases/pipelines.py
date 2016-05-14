# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
import hashlib
import os.path


class DownloadcasesPipeline(object):
    def process_item(self, item, spider):
        return item

class OHCHRFIlesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        #media_guid = hashlib.sha1(url).hexdigest()  # change to request.url after deprecation
        #media_ext = os.path.splitext(url)[1]  # change to request.url after deprecation
        media_guid = hashlib.sha1(url[-100:]).hexdigest()
        media_ext = '.pdf'
        return 'full/%s%s' % (media_guid, media_ext)