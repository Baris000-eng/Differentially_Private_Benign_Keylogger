import pandas as pd

social_media_names = []
visited_websites = []
csv_file_name = "dataset_1.csv"
def csv_to_array(dataset_name : str):
    df = pd.read_csv(dataset_name)
    df = df.dropna(axis=0, how='any')
    websites_list = df["id"].to_list()
    for website in websites_list:
        website_removed_dot = remove_after_dot(website)
        social_media_names.append(website_removed_dot)

def remove_after_dot(website_with_dot : str):
    dot_index = website_with_dot.index(".")
    without_dot = website_with_dot[:dot_index]
    return without_dot

def is_exists_in_database(database_as_array : list(), users_entered_text : str):
    if users_entered_text in database_as_array:
        visited_websites.append(users_entered_text)
        return True
    return False


def main():
    csv_to_array(csv_file_name)
    #is_exists_in_database(social_media_names, )
