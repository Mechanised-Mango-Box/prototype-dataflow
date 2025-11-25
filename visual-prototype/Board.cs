using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;

public class Board
{
	public readonly Dictionary<Guid, NodeData> Nodes;  /// <NodeId, Node>
	public readonly Dictionary<PinAddress, Edge> Edges;  /// <Pin, Edge>
	public readonly Dictionary<string, object> UserVariables;
	// special_variables: /// this should be things like player position

	public void Propagate()
	{
		List<NodeData> frontier = [];

		/// Add all nodes with no dependencies to frontier
		foreach (var node in Nodes.Values)
			if (node.GetResultPins().Length == 0)
				frontier.Add(node);


		/// BFS-like over nodes
		while (frontier.Count > 0)
		{
			bool foundAnyProcessableNode = false;

			foreach (var node in frontier)
			{
				if (IsDependenciesFulfilled(node))
				{
					node.GenerateResults();
					frontier.Remove(node);
					foundAnyProcessableNode = true;
					break;
				}
			}

			if (!foundAnyProcessableNode)
			{
				throw new Exception("Inval ID DAG (probs? deadlock/cycle)");
			}
		}
	}
	public bool IsDependenciesFulfilled(NodeData node)
	{
		/// All args have been connected and have results
		ImmutableArray<PinAddress> inputPins = node.GetArgPins();

		if (inputPins.Length == 0)
		{
			return true;  ///Has no dependencies
		}

		/// Go back up the chain:
		/// [source node] -----> (edge) -----> [node]
		return inputPins.All(argPin =>
			Edges.TryGetValue(argPin, out var sourceEdge) &&
			Nodes.TryGetValue(sourceEdge.Source.OwnerId, out var sourceNode) &&
			sourceNode.HasOutput()
		);
	}


	public void Tick()
	{
		/// TODO cleanup
		/// 1. snapshot world / load sensor data
		/// 2. propagate
		/// 3. tick actuators

		// TODO snapshot data

		Propagate();

		foreach (var node in Nodes)
		{
			// if (issubclass(type(node), Actuator))
			// {
			// node.actuate();
			// }
		}

	}
}