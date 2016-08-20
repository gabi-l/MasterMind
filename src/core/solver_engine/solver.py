"""
Module encapsulating the algorithm that feed the most optimal next turn considering the feedback received
"""
from src.core.play.code import Attempt
from src.core.solver_engine.candidate_manager import CandidateManager
from src.core.play.feedback_generator import FeedbackGenerator
from src.core.play.feedback import Feedback


class Solver(object):
    """
    Class encapsulating the algorithm that feed the most optimal next turn considering the feedback received
    """
    def __init__(self):
        pass

    @staticmethod
    def __get_all_possible_feedbacks():
        return [Feedback(k,l) for k in range(5) for l in range(5-k) if not(k==3 and l==1)]

    @staticmethod
    def elague(attempt, feedback):
        """
        Method elaguing through the current candidates to remove those who would have not gotten the given feedback for the given attempt

        Arguments:
            attempt (Attempt): The attempt associated with the feedback
            feedback (Feedback): The feedback associated with the attempt

        Returns:
             list: A subset list of candidates that would have gotten the feedback on the attempt
        """
        subset = CandidateManager.instance()._get_current_candidates_left()[0:]
        for candidate in CandidateManager.instance()._get_current_candidates_left():
            if FeedbackGenerator.generate_feedback_for_given_code(attempt, candidate.code) != feedback:
                subset.remove(candidate)
        return subset

    @classmethod
    def mini_max(cls):
        """
        Method applying the Mini-Max algorithm to MasterMind's code breaking process to calculate the most optimal next
        attempt considering the current possible candidate

        Returns:
            Attempt: The most optimal attempt considering the current potential candidates left

        Note
        """
        minlist = [[], []]
        candidates = CandidateManager.instance()._get_current_candidates_left()
        if len(candidates) == 1:
            return Attempt(candidates[0], candidates[1], candidates[2], candidates[3])
        for attempt in CandidateManager.instance()._get_all_possible_code():
            best_score = 1296
            for feedback in cls.__get_all_possible_feedbacks():
                attempt_score = len(candidates) - len(cls.elague(attempt, feedback))
                if attempt_score < best_score:
                    best_score = attempt_score
            minlist[0].append(best_score)
            minlist[1].append(attempt)
        best_attempt = minlist[1][minlist[0].index(max(minlist[0]))]
        return Attempt(best_attempt[0], best_attempt[1], best_attempt[2], best_attempt[3])
