import cfscrape
from bs4 import BeautifulSoup
import os , sys
from time import sleep as delay
from urllib.parse import quote_plus,urlencode
from colorama import Fore as cl
from pibyone import loader as ld
from random import choice
class main():
    def __logo__(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        self.Programmer=f"{cl.CYAN}Cyberpunk645"
        self.Team=f"{cl.CYAN}Suskod\u2122\uFE0F"
        self.logo=f"""{cl.CYAN}
╔═╗┬ ┬┌─┐┌─┐┬ ┬  ╔═╗┬ ┬┌─┐
╠═╝│ │└─┐└─┐└┬┘  ║╣ └┬┘├┤ 
╩  └─┘└─┘└─┘ ┴   ╚═╝ ┴ └─┘
{cl.YELLOW}##############################
#  {cl.RED}Programmer{cl.YELLOW}: {self.Programmer}{cl.YELLOW}  #
#  {cl.RED}Team      {cl.YELLOW}: {self.Team}{cl.YELLOW}       #                     
{cl.YELLOW}##############################
\n"""
        for i in self.logo:
            print(i,end="")
            sys.stdout.flush()
            delay(0.0025)
    def __init__(self):
        self.__logo__()
        self.query=input(f"{cl.YELLOW}Dork{cl.RED}: {cl.RESET}")
        self.Page_num=input(f"{cl.YELLOW}Page Numbers{cl.RED}: {cl.RESET}")
        self.save=input(f"{cl.YELLOW}Filename Path{cl.RED}: {cl.RESET}")
        self.cc_p=input(f"{cl.YELLOW}Do you want to use proxies{cl.RED}(yes/no): {cl.RESET}")
        if self.cc_p.startswith("yes"):
            self.ch_proxies=input(f"{cl.YELLOW}Proxies File Path{cl.RED}: {cl.RESET}")
            if os.path.exists(self.ch_proxies):self.f_proxies=open(self.ch_proxies,"r").read().splitlines()
            else:print(f"{cl.YELLOW}[{cl.RED}!{cl.YELLOW}]{cl.RED}This FIle is Not Exist");sys.exit()
        else:self.f_proxies=[""]
        params={"q":self.query,"num":"10000000"}
        res=urlencode(params,quote_via=quote_plus)
        result="https://google.com/search?hl=en&"+res
        self.client=cfscrape.create_scraper()
        final_list=[]
        self.stop_search=False
        
        counter=0
        ld.exec_load("Wait..!", 2)
        for i in range(int(self.Page_num)):
            if not self.stop_search:
                
                rnd_pr=choice(self.f_proxies)
                gg=self.scrape_url(result, counter,rnd_pr)
                final_list=final_list+gg
                counter+=100
            else:break
        ld.exec_load("Saving Urls", 3)
        for i in final_list:
            self.save_file=open(self.save,"a").write(i+"\n")

        print(f"{cl.YELLOW}[{cl.GREEN}*{cl.YELLOW}]{cl.GREEN}Urls  Saved Successfuly on {cl.RESET}{self.save}") 
        

    def scrape_url(self,url,start,proxy):
        url=url+f"&start={start}"
        global s
        s=""
        if proxy =="":proxiesf={"https":""}
        else:proxiesf={"https":f'https://{proxy}'}
        try:
            sreq=self.client.get(url,proxies=proxiesf).text
        except Exception:
            if self.cc_p == "yes":
                print(f"{cl.YELLOW}[{cl.RED}!{cl.YELLOW}]{cl.RED}Error{cl.YELLOW}: {cl.RED}This Proxy is Not Working {cl.RESET}{proxy} ")
            else:
                print(f"{cl.YELLOW}[{cl.RED}!{cl.YELLOW}]{cl.RED}Error{cl.YELLOW}: {cl.RED}Check Connection Network")
            sys.exit()


        get_page_num=""
        
        #sreq=open(os.path.join(os.path.dirname(__file__),"f.html"),"r").read()
        soup=BeautifulSoup(sreq,"html.parser")
        end_page_check=soup.find("div",class_="card-section")
        if "Your search" in str(end_page_check):self.stop_search=True
        else:
            pp=soup.find_all("a",class_="fl",href=True)
            new=[]
            for i in pp:
                if i['href'].startswith("/search?q="):
                    new.append("https://www.google.com"+i['href'])

            for i in soup.find_all("div",class_="yuRUbf"):
                s=f"{s}{i}"

            another_soup=BeautifulSoup(s,"html.parser")
            pp=list(map(self.extrack_url,another_soup.find_all("a",href=True)))
            wwe=list(filter(self.filtring_url, pp))
            return wwe

    

    def extrack_url(self,k):
        return k['href']
    def filtring_url(self,h):

        if (not "webcache.googleusercontent.com" in h) and not "#" in h and not  h.startswith("/search") and not  "translate.google.com" in h:
            
            return h


        

main() 