#!/usr/bin/env python
# -*- coding:utf-8 -*-

#########################################################
# (C) 2000-2021 NSFOCUS Corporation. All rights Reserved#
#########################################################
# import requests
import chardet
import os
import shutil
from os import listdir
from os.path import join
from bs4 import BeautifulSoup


class Scraper(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''

    def scrape_html(self, html):
        bs = BeautifulSoup(html, features="lxml")
        text = bs.get_text(strip=True)
        if text == '':
            bs = BeautifulSoup(html, features="html.parser")
            text = bs.get_text(strip=True)
        return text

    def prepare_smaples(self, sample_path, model_path, categories=None):
        """Load sample files
        """
        target = []
        target_names = []
        filenames = []

        folders = [
            f for f in sorted(os.listdir(sample_path))
            if os.path.isdir(join(sample_path, f))
        ]

        if categories is not None:
            folders = [f for f in folders if f in categories]

        for label, folder in enumerate(folders):
            model_folder = join(model_path, folder)
            if os.path.exists(model_folder):
                shutil.rmtree(model_folder)
            os.mkdir(model_folder)
            target_names.append(folder)
            folder_path = join(sample_path, folder)
            documents = [join(folder, d) for d in sorted(listdir(folder_path))]
            target.extend(len(documents) * [label])
            filenames.extend(documents)

        for filename in filenames:
            try:
                if filename.endswith('html'):
                    with open(join(sample_path, filename), 'rb') as f:
                        html = f.read()
                        result = chardet.detect(html)
                        encoding = result.get('encoding') if result.get(
                            'confidence') > 0.8 else 'utf-8'
                        html = html.decode(encoding, 'strict')
                        text = self.scrape_html(html)
                        # 过滤空文件
                        if text == '':
                            print(filename + "过滤后为空文本")
                        else:
                            with open(join(model_path, filename + '.txt'),
                                      'w',
                                      encoding='utf-8') as f:
                                f.write(text.strip().replace('\n', '').replace(
                                    ' ', ''))
            except (Exception):
                import traceback
                print(filename)
                print(traceback.format_exc())


if __name__ == '__main__':
    scraper = Scraper()
    scraper.prepare_smaples('data_html', 'data_html1')
