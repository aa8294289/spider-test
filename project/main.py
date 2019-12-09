import module.net_link2
import module.parse3
import module.save_text
import module.save_mysql
import module.spider2
import module.content_judge






# 主函数，通过命令行来操作

if __name__ == '__main__':

    print('please give me an url:')
    url=input()
    #module.net_link2.get_link(url)
  #  print('====================================')
   # module.spider2.Html_spider(url)
   # print('======================================')
   # module.parse3.html_parse(url)
    # 匹配网页中的邮箱
    module.parse3.get_mail(url)
    #module.parse3.get_Chineseword(url)
   # module.parse3.str_judge(url)
    #module.parse3.get_URL(url)
   # module.parse3.get_Chineseword(url)
  #  module.parse3.get_URL(url)
  #  module.parse3.str_judge(url)
