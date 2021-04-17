#!/usr/bin/python3

import argparse
import requests
import json

# Default API Key
API_Key = 'a19584b1'
# Default URL
GET_URL = 'https://www.omdbapi.com/?apikey='
# By default, will not show Rotten Tomatoes ratings
Show_Rating = False
# Color based on the row number
G_color_nondefault = '\x1b[33m'
G_color_reset = '\x1b[0m'

def CheckError(resultCode):
    if resultCode != 0:
        exit(1)
    else:
        exit(0)

def search_action(t, string):
    global GET_URL
    global Show_Rating
    global G_color_nondefault
    global G_color_reset
    # Two search types, otherwise error and exit
    search_type = ''
    if t == 'imdb':
        search_type = 'i'
    elif t == 'title':
        search_type = 's'
    else:
        print('Not valid search type: %s' % t)
        CheckError(2)
    # Search string mush be not empty
    if string != '':
        # Get search URL and get result
        URL = GET_URL + '&' + search_type + '=' + string
        res = requests.get(URL)
        # Transfer to json from search result
        movie_info = json.loads(res.content.decode("UTF-8"))
        # If there is valid result, 'Response' will be 'True'
        if movie_info['Response'] == 'True':
            # If search title, return movie list
            if search_type == 's':
                movie_list=[]
                movie_list += movie_info['Search']
                movie_total = int(movie_info['totalResults'])
                # Get all result
                if movie_total > 10:
                    movie_times = movie_total//10
                    movie_left = movie_total%10
                    movie_page = 2
                    while movie_page < movie_times+1 or (movie_left != 0 and movie_page == movie_times+1):
                        URL_Page =  URL + '&page=' + str(movie_page)
                        res = requests.get(URL_Page)
                        # Transfer to json from search result
                        movie_info = json.loads(res.content.decode("UTF-8"))
                        # If there is valid result, 'Response' will be 'True'
                        if movie_info['Response'] == 'True':
                            movie_list += movie_info['Search']
                        movie_page += 1
                return movie_list
            # If search imdb, start to print movide spec
            if search_type == 'i':
                # Spec format
                movie_format = '  {0:12s}  {1:s}'
                # Print header line and -------------
                movie_string = movie_format.format('Spec', 'Description')
                print('\n'+movie_string+'\n'+'-'*68)
                row_num = 0
                for i in movie_info.keys():
                    # Change color based on row number
                    if (row_num % 2) == 1:
                        instance_str1, instance_str2 = G_color_nondefault, G_color_reset
                    else:
                        instance_str1, instance_str2 = '', ''
                    # If the key is not 'Ratings'
                    if i != 'Ratings':
                        # Split spec value
                        movie_spec = movie_info[i].split()
                        movie_spec_num = len(movie_spec)
                        movie_str1, j, num = '', 0, 0
                        while j < movie_spec_num:
                            # Ensure the value including the single element, or should be the full words and less than 50 characters
                            while j < len(movie_spec) and (len(movie_str1+' '+movie_spec[j]) <= 50 or movie_str1 == ''):
                                if movie_str1 == '':
                                    movie_str1 = movie_spec[j]
                                else:
                                    movie_str1 = movie_str1+' '+movie_spec[j]
                                j += 1
                            # When the single element more than 50 characters, need to split to multiple lines
                            m = 0
                            while movie_str1[m*50:(m+1)*50] != '':
                                if num == 0:
                                    # Only first line including spec key
                                    movie_string = movie_format.format(i, movie_str1[m*50:(m+1)*50])
                                    num += 1
                                else:
                                    # The non first line: no spec key
                                    movie_string = movie_format.format(' '*12, movie_str1[m*50:(m+1)*50])
                                print(instance_str1 + movie_string + instance_str2)
                                m += 1
                            movie_str1 = ''
                    # If the key is 'Ratings', need to use Show_Rating to decide 'Rotten Tomatoes'
                    else:
                        num = 0
                        for j in movie_info['Ratings']:
                            for k in j.keys():
                                # If 'Rotten Tomatoes', and Show_Rating False, will break to go next
                                if k == 'Source' and j[k] == 'Rotten Tomatoes':
                                    if not Show_Rating:
                                        break
                                # Only first line including spec key
                                if num == 0:
                                    movie_string = movie_format.format('Ratings', '%-6s: %s' % (k, j[k]))
                                    num += 1
                                # The non first line: no spec key
                                else:
                                    movie_string = movie_format.format(' '*12, '%-6s: %s' % (k, j[k]))
                                print(instance_str1 + movie_string + instance_str2)
                    row_num += 1
                print('')
                CheckError(0)
        # If there is no valid result, 'Response' will be 'False'
        else:
            print('Cannot find any movie math the search condition: %s & %s' % (t, string))
            CheckError(2)
    # Search string mush be not empty, otherwise error and exit
    else:
        print('Not valid search string: %s' % string)
        CheckError(2)

def print_movie(movie_list):
    # This is the function to print movie, will return dict movie_info {num:movie_imdb_id}
    global G_color_nondefault
    global G_color_reset
    # Get the max length of columns for changing the length of ---
    movie_len_t = [len(i['Title']) for i in movie_list]
    movie_len_y = [len(i['Year']) for i in movie_list]
    movie_len_i = [len(i['imdbID']) for i in movie_list]
    movie_len_p = [len(i['Type']) for i in movie_list]
    movie_num = len(movie_list)
    # movie_format is the print format
    movie_format = '  {0:>' + str(len(str(movie_num))) + 's}  {1:' + str(max(movie_len_y)) + 's}  {2:' + str(max(movie_len_i)) + 's}  {3:' + str(max(movie_len_p)) + 's}  {4:s}'
    # Print header line and -------------
    movie_string = movie_format.format('#', 'Year', ' IMDB-ID',  'Type', 'Title')
    print('\n'+movie_string+'\n'+'-'*(12+max(movie_len_t)+max(movie_len_y)+max(movie_len_i)+max(movie_len_p)))
    movie_info = {}
    row_num = 0
    for i in movie_list:
        row_num += 1
        # Change color based on row number
        if (row_num % 2) == 0:
            instance_str1, instance_str2 = G_color_nondefault, G_color_reset
        else:
            instance_str1, instance_str2 = '', ''
        # Get print string and print
        movie_string = movie_format.format(str(row_num), i['Year'], i['imdbID'], i['Type'], i['Title'])
        print(instance_str1 + movie_string + instance_str2)
        # Update dict for return
        movie_info.update({str(row_num): i['imdbID']})
    print('')
    return movie_info

def output_movie(movie_list, filelocation):
    # This is the function to write the movie list to a txt file
    movie_num = len(movie_list)
    fp = open(filelocation, "w")
    # movie_format is the writing format
    movie_format = '{0:>' + str(len(str(movie_num))) + 's}  {1:6s}:  {2:s}'
    for i in range(movie_num):
        fp.write(movie_format.format(str(i+1), 'Title', movie_list[i]['Title'])+'\n')
        fp.write(movie_format.format('', 'Year', movie_list[i]['Year'])+'\n')
        fp.write(movie_format.format('', 'imdbID', movie_list[i]['imdbID'])+'\n')
        fp.write(movie_format.format('', 'Type', movie_list[i]['Type'])+'\n')
        fp.write(movie_format.format('', 'Poster', movie_list[i]['Poster'])+'\n')
    fp.close()
    CheckError(0)

def select_movie(search_word, filelocation):
    # This is the function to make selection
    select = ''
    while select == '':
        # Search movie first
        movie_list = search_action('title', search_word)
        # Print movie list
        if filelocation == '':
            movie_info = print_movie(movie_list)
        # Or write the movie list to file
        else:
            output_movie(movie_list, filelocation)
        count = len(movie_info)
        while select == '':
            # Ask selection
            input_info = '*** Please input the movie number 1-' + str(count) +', r to refresh or q to exit:  '
            movie_select = input(input_info).strip()
            # If 'r', will refresh
            if movie_select == 'r':
                break
            # If 'q', will refresh
            elif movie_select == 'q':
                CheckError(0)
            elif movie_select.isdigit():
                if int(movie_select) >=1 and int(movie_select) <= count:
                    select=movie_info[movie_select]
    # After selection, search movie based on imdb
    search_action('imdb', select)

def parseScriptArguments():
    global API_Key
    global GET_URL
    global Show_Rating
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='api_key', help='API Key for www.omdbapi.com. (optional)')
    parser.add_argument('-s', dest='search_word', help='Word from movie title to search for. (optional)')
    parser.add_argument('-f', dest='filelocation', help='File name to save the result from movie title to search for. (optional)')
    parser.add_argument('-i', dest='search_imdb', help='IMDB ID of movie title to search for. (optional)')
    parser.add_argument('-v', dest='show_rating', help='Whether showing Rotten Tomatoes ratings, false by default (optional)', action='store_true')
    args = parser.parse_args()
    # If search_word and search_imdb are not provided, print help and exit.
    if args.search_word is None and args.search_imdb is None:
        parser.print_help()
        CheckError(1)
    # If API Key is not provided, using default API Key
    if args.filelocation is None:
        args.filelocation = ''
    if args.api_key is None:
        args.api_key = API_Key
    GET_URL += args.api_key
    # Update Show_Rating to non-default
    if args.show_rating:
        Show_Rating = True
    return args

if __name__ == '__main__':
    # Initiate args
    options = parseScriptArguments()
    # Search movie based on imdb
    if options.search_imdb:
        search_action('imdb', options.search_imdb)
    # Search movie based on title
    elif options.search_word:
        select_movie(options.search_word, options.filelocation)
