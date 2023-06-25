class WorkingMemory(dict):
    """Cat's volatile memory.

    Handy class that behaves like a `dict` to store temporary custom data.

    Returns
    -------
    dict[str, list]
        Default instance is a dictionary with `history` key set to an empty list.

    Notes
    -----
    The constructor instantiates a dictionary with a `history` key set to an empty list that is further used to store
    the conversation turns between the Human and the AI.
    """

    def __init__(self):
        # The constructor instantiates a `dict` with a 'history' key to store conversation history
        super().__init__(history=[])

    def update_conversation_history(self, who, message):
        """Update the conversation history.

        The methods append to the history key the last three conversation turns.

        Parameters
        ----------
        who : str
            Who said the message. Can either be `Human` or `AI`.
        message : str
            The message said.
        
        """
        # append latest message in conversation
        self["history"].append({"who": who, "message": message})

        # do not allow more than k messages in convo history (+2 which are the current turn)
        k = 3
        self["history"] = self["history"][(-k - 1):]
