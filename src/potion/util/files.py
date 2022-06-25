import os
import re
import time
import json
import shutil


class Lurk:
    
    
    def __init__(self, 
                 base_dir: str, 
                 blist:list=None, 
                 ldepth:int=2):
        
        self.base_dir = base_dir
        self.blist = blist
        self.ldepth = ldepth
    
    
    
    def ls(self, cur_dir: str = ".") -> []:
        """
            Args: 
                cur_dir is current directory path
                
            Out: 
                list of sub directories (1st level)
        """
        pth = os.path.join(self.base_dir, cur_dir)
        if not os.path.isdir(pth):
            yield cur_dir
        else:
            for pi in os.listdir(pth):
                yield os.path.join(cur_dir, pi)
    
    def isdir(self, cur_dir: str = None) -> bool:
        path = os.path.join(self.base_dir, cur_dir)
        return os.path.isdir(path)
        
    
    def __wls_helper__(self, root, segment, maxdepth):
        dirs = []
        if self.isdir(root):
            if segment == "*":
                dirs = self.ls(root)
            elif segment == "**":
                base = [root]
                for depth in range(maxdepth):
                    tmp = []
                    for d in base:
                        tmp += self.ls(d)
                    base = tmp
                    dirs += base
            elif segment.find("*") >= 0:
                segment = "^" + segment.replace(".", "\\.").replace("*", "(.*)?") + "$"
                dirs = filter(
                    lambda d: re.match(segment, d.split(os.sep)[-1]), self.ls(root))
            elif os.path.exists(os.path.join(root, segment)):
                dirs = [os.path.join(root, segment)]                        
        return list(dirs)
    
    
    def wls(self, wildcard, maxdepth=10):
        segments = wildcard.split(os.sep)
        roots = [""]
        for segment in segments[:-1]: 
            tmp = []
            for root in roots:
                tmp += self.__wls_helper__(root, segment, maxdepth)
            roots = tmp
        files = []
        for root in roots:
            files += self.__wls_helper__(root, segments[-1], maxdepth)
        return files