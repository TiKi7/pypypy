class Points:
    '''
    this is the main class to .......
    storing / adding / calling points
    '''
    # main storage!
    memo = {}
    force=True
    
    def prepare(self, x, y):
        self.address = str(x) + ' ' + str(y)
        self.is_in = True if self.address in self.memo.keys() else False
        return self.is_in
        
    def call (self, x, y):
        #----- prepairing [address] and [is_in]
        self.prepare(x,y)
        #----- code -----#
        if self.is_in:
            return self.memo[ self.address ]
    
    def add (self, x, y, z=0):
        #----- prepairing [address] and [is_in]
        self.prepare(x,y)
        #----- code -----#
        if not self.is_in or self.force:
            self.memo[ self.address ] = z
        else: print('Cant override')
        #----- trash -----#
        #print(self.call(x,y))