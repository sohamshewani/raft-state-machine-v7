# raft.py
import asyncio
from node import Node
from leader_election import LeaderElection
from state_machine import StateMachine
from log_compaction import LogCompaction
from message import Message
from utils import logger

# Global variables
_nodes = {}
_leader = None
_log_compaction = None

async def main(loop, config):
    global _nodes, _leader, _log_compaction
    _nodes = {node_id: Node(node_id, loop) for node_id in config['nodes']}
    _log_compaction = LogCompaction(config['log_compaction'])
    leader_election = LeaderElection(_nodes, loop, config['election_timeout'])
    _leader = await leader_election.start()
    if _leader is None:
        raise Exception(