import util


class Production:
    """Represent tile production layout: plates and center pile.

    From the point of view of the game logic, we do not create new tiles
    anywhere in this class. It only operates on the tiles it is given from
    the outside. It gives away the tiles when requested to."""

    def __init__(self, num_plates):
        self.num_plates = num_plates
        self.plates = [[] for _ in range(num_plates)]
        self.center = []


    def is_correct_move(self, tiles, tiles_type):
        """Verify whether the move to take tiles of tiles_type is correct.
        """
        return tiles_type in tiles


    def take(self, tiles, tiles_type):
        """Take the tiles of the given type and drop others to the center.
        Return the list of tiles taken.
        Throw exception on an incorrect move.

        Note that in the unlikely case if there's only the first move tile left
        in the center, one needs to explicitly pick it up.
        """
        if not self.is_correct_move(tiles, tiles_type):
            raise util.InvalidMoveError(
                "Can't take tiles of type " + str(tiles_type) +
                " from plate having tiles " + str(tiles))
        taken = []
        for t in tiles:
            if t in [util.Tile.FIRST_MOVE, tiles_type]:
                taken.append(t)
            else:
                self.center.append(t)
        return taken


    def take_plate(self, plate_id, tiles_type):
        """Take tiles from a plate and return the list of those taken.
        """
        if plate_id not in list(range(self.num_plates)):
            raise util.InvalidMoveError(
                "There's no plate number " + str(plate_id))
        tiles = self.plates[plate_id][:]
        self.plates[plate_id] = []
        return self.take(tiles, tiles_type)


    def take_center(self, tiles_type):
        """Take tiles from the center.
        Throw exception on an incorrect move.
        """
        tiles = self.center[:]
        self.center = []
        return self.take(tiles, tiles_type)
