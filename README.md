# TIL

-   Organize what you learned on the day

## 2023-03-27

-   git bash Install
-   Linux Command
-   Vim Usage

## 2023-03-28

-   commit
    -   Content
    -   When Create Commit
    -   Commit Size
-   Repo
    -   Content
    -   Different Default Folder & Repo (.git Folder Exist)
    -   git init Command Use Create Repo

## 2023-03-29

-   Commit Making
    -   `git commit -m`
-   Staging Area
    -   `git add` Use the command to add the file to the staging area you want to insert

## 2023-03-31

-   python String methods
-   python String formatting

## 2023-04-12

-   Turtlebot3
    [Setting](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)

## 2023-04-14
### BasicComputerPrograming
-   python tuple (4-5)
```python
tuple = (), tuple(), tuple(list) ...
One Object tuple (a,)  <- not forget ","
```
-   python dictionary
```python
dictionary = { key : value, ... }
```
-   python comprehension
```python
expr for target1 in seq1... if condtition
```
- python fuction
  * built-in function
  ```python
  name(arg1,arg2, ...) // return value
  ```
  * user-defined function
    ```python
    def name(arg1,arg2, ...) :
        body
        return value
    ```
    
## 2023-04-15
### BasicStatistics
- Population
- Sample
- Variance
- Standard deviation

## 2023-04-17
### BasicComputerPrograming

- Exam Solve

## 2023-05-12

- Object, Class, Instance, \_\_INIT\_\_

## 2023-05-19

- Class Inheritance
- Super Class \_\_INIT\_\_
- Private Variable `__(variable)`
- Overriding
- Multi Class Inheritance

## 2023-05-26

- module, package, try ~except, raise

## 2023-06-02

- ```open, read, write, close``` function
- ```writelines, writeline, readlines, readline``` function
- binary file
  ```python 
  open(file,"wb") # Open for Write
  open(file,"rb") # Open for Read
  file.write(bytes)
  file.read(size)
  ```
- struct module

     ```python
    import struct
    
    struct.pack(format, *values)
    struct.unpack(format, bytedata)
  
    struct.calcsize(format)
    ```
- struct format table

| 문자 | 바이트 순서       | 크기와 정렬  |
|--|--------------|---------|
| @/= | 시스템에 따름      | 시스템에 따름 |
| = | 시스템에 따름      | 표준      |
| < | 리틀 엔디안       | 표준      |
| \> | 빅 엔디안        | 표준      |
|! | 네트워크 (빅 엔디안) | 표준      |
- `<` big-endian, `>` little-endian
- str -> byte ``str.encode()``
- byte -> str ``byte_str.decode()``
- file pointer
     ```python
    file.seek(offset,n)
    file.tell() # Pointer Position
    ```