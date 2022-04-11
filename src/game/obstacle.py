from .game_object import GameObject


class Obstacle(GameObject):
    velocity = 0

    def collides_with(self, other: GameObject):
        return self.get_world_hitbox().colliderect(other.get_world_hitbox())

    def update(self, delta_time: float) -> None:
        self.pos.x -= self.velocity * delta_time

    def copy(self):
        obs = Obstacle(self.pos, self.image, self.hitbox)
        obs.collide = self.collide
        return obs

    def collide(self, *args, **kwargs):
        pass
