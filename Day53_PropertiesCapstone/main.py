from google_forms import GoogleForms
from search_zillow_properties import SearchZillowProperties


def main():
    properties = SearchZillowProperties()
    properties.search_properties()
    property_data = properties.make_property_data()

    g = GoogleForms()
    g.max_screen()
    g.update_google_form(property_data=property_data)


if __name__ == '__main__':
    main()
