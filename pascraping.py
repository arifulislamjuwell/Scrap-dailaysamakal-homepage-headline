from pascrap import palog
from pascrap.pascrap import Pascraper
from pascrap import pascrap

palog.add_manual_error_log('html/error.log')

new_scraper= Pascraper(pascrap.url_pa, palog)

new_scraper.retrieve_webpage()
new_scraper.write_page_as_html()

new_scraper.read_page_from_html()
new_scraper.convert_data_to_BS4()
new_scraper.perser_soup_to_normal_html()
