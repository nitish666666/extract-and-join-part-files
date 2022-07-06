import os
import zipfile
import py7zr
import tarfile
import rarfile
from sys import argv
from pathlib import Path

import pathlib
read_buffer_size = 1024
chunk_size = 1024 * 100000


def findsuffix():

    path_location = "movie"
    for file in os.listdir(path_location):
        if file.endswith(".zip"):
            zipextract()
        elif file.endswith(".tar"):
            tarextract()
        elif file.endswith(".rar"):
            rarextract()
        if file.endswith(".7z"):
            sevenzip()

'''
    file_extension = pathlib.Path('D:/pythonProject/movie/oo.rar').suffix

    print("File Extension: ", file_extension)
    if file_extension == '.zip':
        zipextract()
    elif file_extension == '.7z':
        sevenzip()
    elif file_extension == '.tar':
        tarextract()
    elif file_extension == '.rar':
        rarextract()
'''

def zipextract():
    with zipfile.ZipFile('movie/a.zip', 'r') as zip_ref:
        zip_ref.extractall('xzip')
    file_extension = '.zip'
    _join('xzip/oo',file_extension)

def sevenzip():
    with py7zr.SevenZipFile('movie/oo.7z', mode='r') as z:
        z.extractall('x7z')
    file_extension = '.zip'
    _join('x7z/oo',file_extension)

def tarextract():
    tar = tarfile.open('movie/oo1.tar')
    tar.extractall('xtar')
    tar.close()
    file_extension = '.zip'
    _join('xtar/oo',file_extension)

def rarextract():
    rar = rarfile.RarFile('movie/oo.rar')
    rar.extractall('xrar')
    file_extension = '.zip'
    _join('xrar/oo',file_extension)


def _chunk_file(file, extension):
    current_chunk_size = 0
    current_chunk = 1
    done_reading = False
    while not done_reading:
        with open(f'{current_chunk}{extension} file_extension ', 'ab')as chunk:
            while True:
                bfr = file.read(read_buffer_size)
                if not bfr:
                    done_reading = True
                    break

                chunk.write(bfr)
                current_chunk_size += len(bfr)
                if current_chunk_size + read_buffer_size > chunk_size:
                    current_chunk += 1
                    current_chunk_size = 0
                    break


def _join(y,file_extension):
    q = pathlib.Path.cwd()
    p = q / y
    print(p)
    print(file_extension)
    if file_extension == '.zip':
        chunks = list(p.rglob('*.zip'))
    elif file_extension == '.7z':
        chunks = list(p.rglob('*.7z'))
    elif file_extension == '.tar':
        chunks = list(p.rglob('*.tar'))
    elif file_extension == '.rar':
        chunks = list(p.rglob('*.rar'))

    chunks.sort()
    print(chunks)
    extension = chunks[0].suffixes[0]
    i=0

    with open(f'join{i}{extension}', 'ab') as file:
        for chunk in chunks:
            with open(chunk, 'rb')as piece:
                while True:
                    bfr = piece.read(read_buffer_size)
                    if not bfr:
                        break
                    file.write(bfr)
    i+=1



if __name__ == '__main__':
    findsuffix()

