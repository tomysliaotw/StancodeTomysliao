"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
8
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="lxml")

        # ----- Write your code below this line ----- #
        row = soup.find_all(['section', 'div', 'tbody', 'tr'])
        male = 0
        female = 0
        row_count = 0
        for i in row:
            try:
                lis = i.getText().split()
                m_count = int(lis[2].replace(",", ""))
                f_count = int(lis[4].replace(",", ""))
                # print(str(row_count)+": "+str(m_count) + " , " + str(f_count))
                row_count += 1
                if row_count > 1:
                    male += m_count
                    female += f_count
            except IndexError:
                pass
            except ValueError:
                pass
            except TypeError:
                pass
        print('Male:' + str(male))
        print("Female:" + str(female))


if __name__ == '__main__':
    main()
