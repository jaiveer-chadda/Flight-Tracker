
with open("../resources/airports/GlobalAirportDatabase/GlobalAirportDatabase.txt") as file:
    database_lines = file.read().split("\n")
    
list_to_upload: list[str] = []

for line in database_lines:
    if line == "":
        continue
    raw_data = line.split(":")
    if raw_data[14] == "0.000" and raw_data[15] == "0.000":
        continue
    data = (
        raw_data[0].upper(),
        raw_data[2].title(),
        raw_data[3].title(),
        raw_data[4].title(),
        raw_data[14],
        raw_data[15]
    )
    list_to_upload.append(",".join(data))


with open("../resources/airports/usable_database.txt", "w") as file:
    file.write("\n".join(list_to_upload))
