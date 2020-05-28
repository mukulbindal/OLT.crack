3
*��^�  �               @   s�  d dl Zd dlZd dlZd dlZdddddddddd	d
d�Zdd� Zdd� Zdd� Z	e
dk�r�eed d ed  ed  d ed  �Zeed d ed  �Zg Zedk�red� ed� e	� Zedkr�ed� ed � ee�Zed� eed d  ed  � nNed!� yed"d#�Zeje�ZW n,   eed$ d% ed  � ed � Y nX yxee� �qZW W n ek
�r�   ed&� Y nX dS )'�    Nz[95mz[94mz[91mz[93mz[92mz[96mz[0mz[1mz[4m)ZHEADERZOKBLUEZRED�OKYELLOW�GREEN�	LIGHTBLUE�WARNING�FAIL�ENDCZBOLDZ	UNDERLINEc             C   s�   y�dg}t td��}ttd d � tdtd  � x`t|�D ]T}tj� }tj|�}tj	| � |j
|� ttd d t|d	 � d
d� tjj�  q>W tdtd  � tdd�}tj||� |S    ttd d td  � tdd�}tj||� |S d S )N� zEnter the number of questionsr   z)[+] Please wait while collecting data....zP[+] Collecting data. Please do not touch the mouse or keyboard until it is done!r   r   zCollecting Question �   � )�endz0
[+] Data collected successfully.. Saving data..zquestions.json�wr   z9[!] Somehow program Crashed! Saving the collected data...)�int�input�print�colors�range�pgZ
screenshot�ptZimage_to_stringZclick�append�str�sys�stdout�flush�open�json�dump)�location�l�t�i�image�text�f� r#   �	master.py�gather_data   s*    


 

r%   c             C   s^   t td d td  �}x@tt| ��D ]0}|| | kr&ttd d t|� td  � q&W d S )Nr   z;[+] Enter the keywords to search. Press CTRL + C to quit>> r   r   zFound Match in )r   r   r   �lenr   r   )r   �sr   r#   r#   r$   �answerQueries)   s    r(   c              C   s�   d} t j| dd�}|d kr\ttd d td  � ttd d td  �}|d	krXt� S d S ttd d
 t|� � tdtd  � t j|� |S )Nz
button.pngg      �?)Z
confidencer   z[[!] Could not detect Save & Next Button..
[!] Please make sure it is visible on the screen.r   r   z"[+] Do you want to try again(Y/N)?ZyYz[+] Next button found at z"[+] Now move to the first question)r   ZlocateCenterOnScreenr   r   r   �detect_save_and_submitr   ZmoveTo)r    r   Ztryagainr#   r#   r$   r)   /   s    
r)   �__main__r   z�[+] Welcome! Please login to the exam and open terminal & browser in split screen mode. Make Sure that Questions and Save&Next Button are visible.
r   r   z[+] Hit Enter once done that.r   zM[+] Is it a new exam or you have already saved any data before(Enter 1 or 2)?�1z[+] Creating new Exam....Done!z$[+] Detecting Save & Next Button....z[-] Exiting the program...z#[+] Now you can enter the queries..r   zK[!] Note that if the program was crashed, it won't answer all the queries..z#[+] Detecting already save files...zquestions.json�rr   z([!] Could not find any file... Exiting..z
[+] Quitting the program...)Zpytesseractr   Z	pyautoguir   r   r   r   r%   r(   r)   �__name__r   ZqueryZisFirstTimer   r   Zsaveandnext�exitr   r"   �load�KeyboardInterruptr#   r#   r#   r$   �<module>   sV   
,

