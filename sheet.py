import datetime
import pygsheets
from models import Sounds, Netflilx, Haveyouever

def update_netflix(netflixResponse: Netflilx):
    """
    save rating results for Netflops pitch ==> H1
    """
    wks = get_worksheet_by_name('Scoring Board', 'Netflop Pitch')
    line_index = find_empty(wks, 'H', 2)

    list_items = list('IJKLMN0PQRS')

    wks.unlink()
    wks.update_value('H' + line_index, str(datetime.datetime.now()))
    for i, letter in enumerate(list_items):
        if  i < len(netflixResponse.order):
            wks.update_value(letter + line_index, netflixResponse.order[i])
    wks.link()

def update_sounds(soundsResponse:Sounds):
    """
    save results for what's that sound ==> K13
    """
    wks = get_worksheet_by_name('Scoring Board', 'What\'s That Sound?')
    line_index = find_empty(wks, 'K', 13)

    wks.unlink()
    wks.update_value('K' + line_index, str(datetime.datetime.now()))
    wks.update_value('L' + line_index, soundsResponse.team)
    wks.update_value('M' + line_index, soundsResponse.sound1)
    wks.update_value('N' + line_index, soundsResponse.sound2)
    wks.update_value('O' + line_index, soundsResponse.sound3)
    wks.update_value('P' + line_index, soundsResponse.sound4)
    wks.update_value('Q' + line_index, soundsResponse.sound5)
    wks.update_value('R' + line_index, soundsResponse.sound6)
    wks.link()

    pass

def get_questions(type):
    """
    get initial list to show, based on @type
    """
    res = ""
    
    if(type == "haveyouever"):
        wks = get_worksheet_by_name('Scoring Board', 'Have You Ever?')
        res = wks.get_values("AG5", "AG25")

    if(type == "movies"):
        wks = get_worksheet_by_name('Scoring Board', 'review-names')
        res = wks.get_values("A1", "A12")

    return res

def update_hye(hyeResponse: Haveyouever):
    """
    put answers for 'Have you ever' game => J20....J25
    """
    
    wks = get_worksheet_by_name('Scoring Board', 'Have you ever Form')

    list_items = list('BCDEFGH')

    line_index = find_empty(wks, 'A', 2)

    wks.unlink()
    wks.update_value('A' + line_index, str(datetime.datetime.now()))
    for i, value in enumerate(hyeResponse.answers):
        if  i < len(hyeResponse.answers):
            wks.update_value(list_items[i] + str(line_index), value)
    wks.link()


def find_empty(wks, start_col, start_line = 0):
    """
    find next empty line
    """
    i = start_line
    g_val = ""
    while (i < 20):
        g_val = wks.get_value(start_col + str(i))
        #print(i, g_val)
        if(g_val == ""):
            break
        i += 1
    
    return str(i)

def get_worksheet_by_name(file, wks_title):
    gc = pygsheets.authorize()
    sh = gc.open(file)
    wks = sh.worksheet_by_title(wks_title)
    return wks

def get_sheet():
    gc = pygsheets.authorize()
    sh = gc.open('test data read - 1y_jG1j9VXJGPpAAo8eFnYeQqPKI2Z')
    wks = sh.sheet1
    return wks