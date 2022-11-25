import os
import json
import pandas as pd

path = os.getcwd()

# Open the file in read mode
with open(path + '/poemTags.json', 'r') as f:
    # Read the file
    data = f.read()
    # Load the JSON to a Python list & dump it as CSV
    mylist = json.loads(data)


    # Open a file to write the CSV to
    with open(path + '/poemTags.csv', 'w') as f:
        # write ",text" to the first line
        f.write(',text')

        # initialize a counter
        i = 0
        # Loop through the list
        for item in mylist:
            # for each item in item[tags]
            for tag in item['tags']:
                # create a string with the format "tag,poem"
                string_line_with_markers = '"<|endoftext|>' + tag + ':'+ item['poem'] + '<|endoftext|>"'
                #  write counter, string to the file
                f.write('\n' + str(i) + ',' + string_line_with_markers)

                # increment the counter
                i += 1

        # Close the file
        f.close()


df = pd.read_csv(path + '/poemTags.csv')

# shuffle the dataframe and let index start from 0
df = df.sample(frac=1).reset_index(drop=True)

# divide the dataframe into 80% train and 20% test
train_df = df[:int(len(df)*0.8)]
test_df = df[int(len(df)*0.8):]

# drop unnamed column
train_df = train_df.drop(columns=['Unnamed: 0'])
test_df = test_df.drop(columns=['Unnamed: 0'])

# rename the indeex column to empty string
train_df = train_df.rename(columns={'index': ''})
test_df = test_df.rename(columns={'index': ''})

# save the dataframes as csv
train_df.to_csv(path + '/poem_train.csv')
test_df.to_csv(path + '/poem_test.csv')




                
    


        
