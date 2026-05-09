import 'package:flutter/material.dart';
import 'screens/search_screen.dart';

void main() => runApp(AirTicketApp());

class AirTicketApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Air Ticket Booking',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: SearchScreen(),
    );
  }
}
