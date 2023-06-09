# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits
from util.objects import Vector3
from util.routines import goto
from util.tools import rotate_vector

class Bot(GoslingAgent):
    
    def run(self):
        # set_intent tells the bot what it's trying to do
        self.print_debug()
        self.renderer.draw_line_3d(self.me.location, self.ball.location,self.renderer.white())
        if self.get_intent() is not None:
            self.debug_intent()
            return
        # d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        # d2 = abs(self.me.location.y - self.foe_goal.location.y)
        # is_in_front_of_ball = d1 > d2

        # if self.kickoff_flag:
        #    self.set_intent(kickoff())
        #    return
        # if self.is_in_front_of_ball():
        #     self.set_intent(goto(self.friend_goal.location))
        #     self.debug_text = "rotating to goal"
        #     return

        # if self.me.boost == 100:
        #     self.set_intent(short_shot(self.foe_goal.location))
        #     self.debug_text = "taking a shot"
        #     return

        # closest_boost = self.get_closest_large_boost()
        # if closest_boost is not None:
        #     self.set_intent(goto(closest_boost.location))
        #     self.debug_text = "getting boost"
        #     return
        
        if self.kickoff_flag:
            closest_boost = self.get_closest_large_boost()
            self.set_intent(goto(closest_boost.location))
            return
        if self.me.boost != 0:
            center_field = Vector3(0, 0, 0)
            right_wall_vector = Vector3(0, 1, 0)
            target_orientation = rotate_vector(right_wall_vector, self.me.rotation.yaw)
            self.set_intent(goto(center_field, target_orientation))
            # self.set_intent(goto(Vector3(0,0,0),Vector3(500, 500, 0)))
            # self.push(goto())
            return


        
        
        
        
        
        
        
        
        
        
        
        # targets = {
        #     'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
        #     'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        # }
        # hits = find_hits(self,targets)
        # if len(hits['at_opponent_goal']) > 0:
        #     self.set_intent(hits['at_opponent_goal'][0])
        #     print("at their goal")
        #     return
        # if len(hits['away_from_our_net']) > 0:
        #     print("away from our goal")
        #     self.set_intent(hits['away_from_our_net'][0])
        #     return
        # if self.time % 2 == 0:
        #     print(hits)
        # self.set_intent(atba())



        # if is_in_front_of_ball:
        #     self.set_intent(goto(self.friend_goal.location))
        #     return
        # self.set_intent(short_shot(self.foe_goal.location))
