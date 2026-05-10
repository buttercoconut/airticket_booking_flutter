import 'package:flutter/material.dart';
import '../models/flight.dart';

class FlightCard extends StatelessWidget {
  final Flight flight;
  final VoidCallback onTap;

  const FlightCard({Key? key, required this.flight, required this.onTap})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 12),
      child: ListTile(
        leading: const Icon(Icons.flight, color: Colors.blueAccent),
        title: Text('${flight.airline} • ${flight.flightNumber}'),
        subtitle: Text(
            '${flight.departureCity} → ${flight.arrivalCity}\n${flight.departureTime} – ${flight.arrivalTime}'),
        trailing: Text('\$${flight.price.toStringAsFixed(2)}',
            style: const TextStyle(fontWeight: FontWeight.bold)),
        onTap: onTap,
      ),
    );
  }
}
