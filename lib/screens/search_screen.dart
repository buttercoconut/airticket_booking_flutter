import 'package:flutter/material.dart';
import '../widgets/flight_search_form.dart';
import '../widgets/flight_list.dart';

class SearchScreen extends StatefulWidget {
  @override
  _SearchScreenState createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  List<Map<String, dynamic>> _searchResults = [];

  void _onSearch(String origin, String destination, DateTime date) {
    // Dummy data for demonstration
    setState(() {
      _searchResults = [
        {
          'flightNumber': 'AB123',
          'origin': origin,
          'destination': destination,
          'date': date.toIso8601String(),
          'price': 199.99,
        },
        {
          'flightNumber': 'CD456',
          'origin': origin,
          'destination': destination,
          'date': date.toIso8601String(),
          'price': 249.99,
        },
      ];
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Search Flights')),
      body: Column(
        children: [
          FlightSearchForm(onSearch: _onSearch),
          Expanded(child: FlightList(flights: _searchResults)),
        ],
      ),
    );
  }
}
