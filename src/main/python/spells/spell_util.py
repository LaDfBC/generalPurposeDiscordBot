from python.sheets.sheets_util import get_gspread_service

key = '1cuwb3QSvWDD7GG5McdvyyRBpqycYuKMRsXgyrvxvLFI'
base_url = 'https://www.d20pfsrd.com/magic/all-spells/'

def get_spell_message(content, author):
    print("Fetching..." + content + " for " + author)
    data = __fetch_data(__parse_spell_message(content))

    if data is None:
        return ", I can't find that spell for you.  Maybe the site is down?"
    else:
        message = ", Here's some basic info for you about " + data['name'] + ":\n" + \
        "School: " + data['school'] + '\n' + \
        "Cast Time: " + data['casting_time'] + '\n' + \
        "Range: " + data['range'] + '\n' + \
        "Short Description: " + data['short_description'] + '\n' + \
        "And the URL can be found here: " + data['url'] + '\n'

    return "<@" + str(author) + ">" + message

def __parse_spell_message(content):
    space_index = content.find(' ')
    spell = content[space_index:].strip()
    return spell

def __fetch_data(spell):
    first_letter = spell[0]
    url = base_url + first_letter + '/' + spell.replace(' ', '%20')

    sheets_client = get_gspread_service()
    worksheets =  sheets_client.open_by_key(key).worksheets()

    data = {}

    for worksheet in worksheets:
        if worksheet.title != 'Notes':
            try:
                cell = worksheet.find(spell)
            except:
                return None

            row = cell.row
            data['name'] = spell
            data['school'] = worksheet.cell(row, 2).value
            data['spell_level'] = worksheet.cell(row, 5).value
            data['casting_time'] = worksheet.cell(row, 6).value
            data['range'] = worksheet.cell(row, 9).value
            data['short_description'] = worksheet.cell(row, 45).value
            data['url'] = url

    return data

if __name__ == '__main__':
    print(get_spell_message('!spell Mad Monkeys'))
