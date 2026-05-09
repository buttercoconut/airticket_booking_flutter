import 'package:flutter/material.dart';
import '../models/flight.dart';

class FlightCard extends StatelessWidget {
  final Flight flight;

  const FlightCard({Key? key, required this.flight}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8),
      child: ListTile(
        title: Text('${flight.airline} ${flight.flightNumber}'),
        subtitle: Text('${flight.origin} → ${flight.destination}'),
        trailing: Text('${flight.price} USD'),
        onTap: () {
          // TODO: navigate to booking screen
        },
      ),
    );
  }
}
