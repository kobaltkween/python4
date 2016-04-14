class Publisher:
    def __init__(self):
        self.subscribers = []
        self.unsubs = []
        self.publishing = False
    
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed.")
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        """Raise a ValueError if subscriber isn't subscribed.
        Add subscriber to the self.unsubs list if publishing.
        If not publishing, remove from the subscriber list
        and, if necessary, the self.unsubs list."""
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers.")
        if self.publishing:
            self.unsubs.append(subscriber)
        else:
            self.subscribers.remove(subscriber)
            if subscriber in self.unsubs:
                self.unsubs.remove(subscriber)
    
    def publish(self, s):
        #Process any unsubscriptions before publishing
        for unsub in self.unsubs:
            self.unsubscribe(unsub)
        # Set publishing to True before publishing and to False again after.
        # I'm not sure I trust the timing on this but it seems to work.
        self.publishing = True
        for subscriber in self.subscribers:
            subscriber(s)
        self.publishing = False
        

if __name__ == "__main__":
    def multiplier(s):
        print(2 * s)
        
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.process)
            self._processed = 0
            
        def process(self, s):
            """
            Problem with simply unsubscribing in this method:
            It alters the subscriber array as the publisher is going through the array.
            So it skips over the subscriber after the first one removed, 
            then hits that subscriber on the round after that, then works properly.
            Unsubscribing shouldn't happen at the same time as publishing.  
            The publisher should process any backlogged unsubscriptions before publishing.  
            It should also block unsubscriptions while publishing.
            """

            self._processed += 1
            if self._processed <= 3:
                print(self.name, ":", self._processed, s.upper())
            else:
                self.publisher.unsubscribe(self.process)
                
        def __repr__(self):
            return self.name
            
    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
    def foo():
        pass
    try: 
        publisher.unsubscribe(foo)
    except ValueError as e:
        print(str(e), "Foo is not a subscriber")