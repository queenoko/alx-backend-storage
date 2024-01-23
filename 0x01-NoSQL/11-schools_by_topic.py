#!/usr/bin/env python3
"""
This script returns list of schools having a specific topic
Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be a pymongo collection object
topic (String) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    Prototype: def schools_by_topic(mongo_collection, topic):
    will return list of schools having a specific topic...
    """
    return mongo_collection.find({"topics": topic})
