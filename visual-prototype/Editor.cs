using System;
using System.Collections.Immutable;
using Godot;

public partial class Editor : Node
{
	[Export] public GraphEdit graphEdit;
	Board board = new();

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		#region Generate board (replace with load from json later)
		NodeData n1 = new(Guid.NewGuid(), NodeType.CONSTANT, Vector2.Zero); board.Nodes.Add(n1.Id, n1);
		NodeData n2 = new(Guid.NewGuid(), NodeType.CONSTANT, Vector2.Zero); board.Nodes.Add(n2.Id, n2);
		NodeData n3 = new(Guid.NewGuid(), NodeType.LOGICAL_OR, Vector2.Zero); board.Nodes.Add(n3.Id, n3);
		NodeData n4 = new(Guid.NewGuid(), NodeType.LOGICAL_AND, Vector2.Zero); board.Nodes.Add(n4.Id, n4);
		NodeData n5 = new(Guid.NewGuid(), NodeType.PRINT, Vector2.Zero); board.Nodes.Add(n5.Id, n5);

		Edge e1 = new(new(n1.Id, "value"), [new(n3.Id, "a")]); board.Edges.Add(e1.Source, e1);
		Edge e2 = new(new(n2.Id, "value"), [new(n3.Id, "b"), new(n4.Id, "b")]); board.Edges.Add(e2.Source, e2);
		Edge e3 = new(new(n3.Id, "value"), [new(n4.Id, "a")]); board.Edges.Add(e3.Source, e3);
		Edge e4 = new(new(n5.Id, "value"), [new(n5.Id, "in")]); board.Edges.Add(e4.Source, e4);
		#endregion

		#region Generate Graph
		foreach (var node in board.Nodes.Values)
		{
			GraphNode gn = new();
			graphEdit.AddChild(gn);

			/// TODO new GraphNodePlus(title, leftPins, rightPins);
			gn.Title = node.Id.ToString();

			ImmutableArray<PinConfig> argPins = node.GetArgPins();
			ImmutableArray<PinConfig> resultPins = node.GetResultPins();
			int maxPinsCount = argPins.Length > resultPins.Length ? argPins.Length : resultPins.Length;
			for (int i = 0; i < maxPinsCount; i++)
			{
				MarginContainer marginContainer = new();
				gn.AddChild(marginContainer);
				if (i < argPins.Length)
				{
					Label labelLeft = new();
					labelLeft.HorizontalAlignment = HorizontalAlignment.Left;
					labelLeft.Text = argPins[i].PinLabel;
					marginContainer.AddChild(labelLeft);
					gn.SetSlotEnabledLeft(i, true);
				}

				if (i < resultPins.Length)
				{
					Label labelRight = new();
					labelRight.HorizontalAlignment = HorizontalAlignment.Right;
					labelRight.Text = resultPins[i].PinLabel;
					marginContainer.AddChild(labelRight);
					gn.SetSlotEnabledRight(i, true);
				}
			}

		}
		#endregion
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}
