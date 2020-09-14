"""
See the problem description at: https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
See the comments in the solution.
"""

# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.buf4 = [''] * 4                # Initializes buf4
        self.buf4_chars_read = 0            # Once read4(buf4), this tracks no of chars read from buf4
        self.buf4_chars_yet_to_read = 0     # Once read4(buf4), this tracks no of chars has yet to be read from buf4
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """        
        write_ptr = 0           # Pointer that counts the no of chars written to buf
        if write_ptr < n:       # If n = 0, no reads and writes are done
            if self.buf4_chars_yet_to_read > 0:             
                while self.buf4_chars_yet_to_read > 0: # First, copy remaining chars, if any, from the previous call of 'read'
                    buf[write_ptr] = self.buf4[self.buf4_chars_read]
                    write_ptr += 1
                    self.buf4_chars_read += 1
                    self.buf4_chars_yet_to_read -= 1
                    if write_ptr == n: return write_ptr

            n_read_chars = 4    # no of read chars using read4. Set to 4 to ensure while is executed given write_ptr < n
            while n_read_chars == 4 and write_ptr < n:  # n_read_chars != 4 means all chars in the file are read
                n_read_chars = read4(self.buf4)
                self.buf4_chars_yet_to_read = n_read_chars
                self.buf4_chars_read = 0
                for i in range(n_read_chars):
                    buf[write_ptr] = self.buf4[i]
                    write_ptr += 1
                    self.buf4_chars_yet_to_read -= 1
                    self.buf4_chars_read += 1
                    if write_ptr == n: return write_ptr
                    
        return write_ptr        
