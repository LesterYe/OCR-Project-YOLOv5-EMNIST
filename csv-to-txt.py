import os
import csv

directory = (
    "C:\GitHub\OCR-Project\EMNIST_Object_Detection_in_TensorFlow\Annotations_Simple"
)

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # filepath = os.path.join(directory, filename)
        csv_file = filename
        txt_file = filename.split(".")[0] + ".txt"
        with open(txt_file, "w") as my_output_file:
            with open(csv_file, "r") as my_input_file:
                [
                    my_output_file.write(" ".join(row) + "\n")
                    for row in csv.reader(my_input_file)
                ]
            my_output_file.close()


# #TEST individual files
# filename = '009999.csv'
# csv_file = filename
# txt_file = filename.split('.')[0] + '.txt'

# with open(txt_file, "w") as my_output_file:
#   with open(csv_file, "r") as my_input_file:
#     [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file) ]
#   my_output_file.close()
