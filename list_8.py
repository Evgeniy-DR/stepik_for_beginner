n = int(input())
list_enter = []

# Input elements into the list
for i in range(n):
    k = input()
    list_enter.append(k)

count_search = int(input())
list_search = []

# Input the search terms
for j in range(count_search):
    search = input().lower()
    list_search.append(search)

# Initialize an empty list to store lines with all search terms
list_no_double = []

# Check if all search terms are present in each line
for line in list_enter:
    original_line = line  # Store the original line with its capitalization
    line = line.lower()  # Convert to lowercase for search comparison
    all_search_terms_present = True
    for search in list_search:
        if search not in line:
            all_search_terms_present = False
            break
    if all_search_terms_present:
        list_no_double.append(original_line)  # Append the original line with its original capitalization

# Print the lines with all search terms
print(*list_no_double, sep='\n')
