**Jakub Janus**

jakub.janus@uek.krakow.pl

### `zoom_chat_to_list.py`
 ---
* This short program creates an xlsx table - **an automated attendance list** - based on messages sent via the public chat in Zoom, using `Numpy` and `Pandas` libraries.
* The automation may be used to check attendance during Zoom meetings (e.g., online classrooms), with specific cut-off times for a beginning and an end of a given meeting.
* It lists the unique names of participants (in alphabetical order) and the exact time of their messages.
* It skips the messages sent outside of a given timeframe or via the private chat in Zoom.
* `chat.txt` file provided [here](https://drive.google.com/file/d/1xag5k6HiUDRi_9yu8fzjm9G9N4E12lI0/view?usp=sharing) contains artificial data to illustrate the outcomes of the program.
---
### To do
0. Ask all the participants of your Zoom meeting to confirm their presence by writing in the public chat at the beginning and - if you prefer to do so - at the end of your Zoom meeting (e.g., ask them to write "present!"). The recommended Zoom login format is "Name Surname".
1. Export `chat.txt` file from a Zoom meeting.
2. If in Google Colab, drop `chat.txt` file from Zoom to `Files` in the left-hand side panel. (Copy it to the folder containing the `main.py` file when using your own machine. You may also source it in any other way.)
3. Run the program.
4. If needed, specify cut-off times for attendance (maximum and minimum time of a message sent in the public chat).
5. Done - your list is printed and `list.xlsx` is ready for download. (Or written in your folder.)

 ---
 *Comments welcome*
