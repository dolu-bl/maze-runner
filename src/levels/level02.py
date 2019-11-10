# -*- coding: utf-8 -*-


class Level02():
    def __init__(self):
        self.order = 1
        self.data = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                    ,[1,2,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1]
                    ,[1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1]
                    ,[1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1]
                    ,[1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1]
                    ,[1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1]
                    ,[1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1]
                    ,[1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1]
                    ,[1,0,1,0,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1]
                    ,[1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1]
                    ,[1,0,1,1,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1]
                    ,[1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1]
                    ,[1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,1]
                    ,[1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1]
                    ,[1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1]
                    ,[1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1]
                    ,[1,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1]
                    ,[1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,1]
                    ,[1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1]
                    ,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1]
                    ]

    def width(self):
        return self.data[0].__len__()

    def height(self):
        return self.data.__len__()
