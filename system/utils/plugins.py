"""
自定义的分页组件 和 md5加密
"""

from django.utils.safestring import mark_safe
from django.conf import settings
import hashlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()

class Pagination(object):

    def __init__(self, request, data_all_list, page_size=10, plus=4):
        self.page = request.GET.get('page', '1')
        self.search_data = request.GET.get('q', '')

        if self.page.isdecimal():
            self.page = int(self.page)
        else:
            self.page = 1

        self.page_size = page_size

        if data_all_list.count() % page_size != 0:
            self.page_max = data_all_list.count() // page_size + 1
        else: self.page_max = data_all_list.count() // page_size

        self.page_list = [self.page + i for i in range(-plus, plus+1)]
        self.page = max(1, self.page)
        self.page = min(self.page_max, self.page)
        self.l = (self.page - 1) * self.page_size
        self.r = self.page * self.page_size
        try:
            self.data_list = data_all_list[self.l: self.r]
        except:
            self.data_list = None

    def html(self):
        page_str_list = []

        for P in self.page_list:
            ele = ''
            if 0 < P <= self.page_max and P != self.page:
                ele = '<li><a href="?q={}&page={}">{}</a></li>'.format(self.search_data, P, P)
            elif 0 < P <= self.page_max and P == self.page:
                ele = '<li class="active"><a href="?q={}&page={}">{}</a></li>'.format(self.search_data, P, P)
            page_str_list.append(ele)

        ele = '<li><a href="?q={}&page={}" aria-label="Next"><span aria-hidden="true">尾页</span></a></li>'.format(self.search_data, self.page_max)
        page_str_list.append(ele)

        page_string = mark_safe("".join(page_str_list))
        return page_string



def check_code(width=120, height=30, char_length=5, font_file='Monaco.ttf', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndChar():
        """
        生成随机字母
        :return:
        """
        return chr(random.randint(65, 90))

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text((i * width / char_length, h), char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rndColor())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)


